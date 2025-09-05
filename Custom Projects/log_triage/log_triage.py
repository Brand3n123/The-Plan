blocked_lines_list = []
query_lines_list = []
domain_counts = {}
source_counts = {}
total = 0
skipped = 0

def parse_line(line):
    parts = line.strip().split()
    blocked_line = {}
    queried_line = {}

    if "blocked" in parts:
        blocked_line["ACTION"] = parts[5]
        blocked_line["DESTINATION"] = parts[6]
        if parts[6] not in domain_counts:
            domain_counts[parts[6]] = 1
        elif parts[6] in domain_counts:
            domain_counts[parts[6]] += 1
        if parts[8] == "0.0.0.0":
            blocked_line["SOURCE"] = "any"
        else:
            blocked_line["SOURCE"] = parts[8]
            if parts[8] not in source_counts:
                source_counts[parts[8]] = 1
            elif parts[8] in source_counts:
                source_counts[parts[8]] += 1
        blocked_lines_list.append(blocked_line)
        return True
    elif "query[A]" in parts:
        queried_line["ACTION"] = "query"
        queried_line["DESTINATION"] = parts[5]
        queried_line["SOURCE"] = parts[7]
        if parts[5] not in domain_counts:
            domain_counts[parts[5]] = 1
        elif parts[5] in domain_counts:
            domain_counts[parts[5]] += 1
        if parts[7] not in source_counts:
            source_counts[parts[7]] = 1
        elif parts[7] in source_counts:
            source_counts[parts[7]] += 1  
        query_lines_list.append(queried_line)
        return True
    else:
        return False
try:
    with open("sample_pihole.log") as pihole_log:
        for line in pihole_log.readlines():
            total += 1
            if not parse_line(line):
                skipped += 1
        top_domains = sorted(domain_counts.items(), key = lambda item : item[1], reverse = True)[:5]
        top_sources = sorted(source_counts.items(), key = lambda item : item[1], reverse = True)[:5]

    with open("top_domains.txt", "w") as domains_txt:
        domains_txt.write("Top Domains:")
        for domain, count in top_domains:
            domains_txt.write(f"\n{domain}: {count}")
        domains_txt.write("\n\nTop Sources:")
        for source, count in top_sources:
            domains_txt.write(f"\n{source}: {count}")

    with open("summary.txt", "w") as summary_txt:
        summary_txt.write(f"Total : {total} log entries")
        summary_txt.write(f"\nParsed : {len(blocked_lines_list) + len(query_lines_list)} lines")
        summary_txt.write(f"\nSkipped : {skipped} blank entries")
        summary_txt.write(f"\nAllowed : {len(query_lines_list)} requests")
        summary_txt.write(f"\nBlocked : {len(blocked_lines_list)} requests")       

except FileNotFoundError:
    print("File not found. Please try again.")

print("Done. Created summary.txt and top_domains.txt")