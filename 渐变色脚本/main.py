list1 = [
    "#f7ce6c",
    "#ff9a9e",
    "#84fab0",
    "#e0c3fc",
    "#30cfd0",
    "#cd9cf2",
    "#9795f0",
    "#e8198b",
    "#b3ffab",
    "#2CD8D5",
    "#5271C4",
    "#69EACB",
]
list2 = [
    "#ff7777",
    "#fad0c4",
    "#8fd3f4",
    "#8ec5fc",
    "#330867",
    "#f6f3ff",
    "#fbc8d4",
    "#c7eafd",
    "#12fff7",
    "#C5C1FF",
    "#B19FFF",
    "#EACCF8",
]

file = open('index.html', 'w', encoding="utf-8")
for i in range(len(list1)):
    file.write(
        '<li>\n'
        '   <p>{}&nbsp;&nbsp;&nbsp;{}</p>\n'
        '   <div class="box" style="background-image: linear-gradient(45deg,{},{})">\n'
        '   </div>\n'
        '   </li>\n'.format(
            list1[i], list2[i], list1[i], list2[i]))
file.close()
