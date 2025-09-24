# Raw input string: "Title:Poet:Year" triplets separated by commas
highlighted_poems = (
    "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, "
    "Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   "
    "Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, "
    "Mr. Grumpledump's Song:Shel Silverstein:2004, "
    "Angel Sound Mexico City:Carmen Boullosa:2013, "
    "In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, "
    "Dreamwood:Adrienne Rich:1987"
)

# Split the big string on commas, creating list of "Title:Poet:Year" entries
highlighted_poems_list = highlighted_poems.split(",")

# Strip whitespace around each entry so later splits are clean
highlighted_poems_stripped = []
for entry in highlighted_poems_list:
    highlighted_poems_stripped.append(entry.strip())

# Split each cleaned entry on ":" creating "Title", "Poet", "Year"
highlighted_poems_details = []
for item in highlighted_poems_stripped:
    highlighted_poems_details.append(item.split(":"))

# Build variables and separate columns for readability and later use
titles = []
poets = []
dates = []

for detail in highlighted_poems_details:
    titles.append(detail[0])
    poets.append(detail[1])
    dates.append(detail[2])

# Print neat sentences using .format()
for i in range(len(titles)):
    print("The poem {} was published by {} in {}."
          .format(titles[i], poets[i], dates[i]))