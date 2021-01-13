haiku1 = {
    "title" : "January",
    "poem" : """Delightful display
                Snowdrops bow their pure white heads
                To the sun's glory."""
}
haiku2 = {
    "title" : "Together",
    "poem" : """You and me alone
                Madness of world locked away
                Peace and quiet reigns"""
}
haiku3 = {
    "title" : "One Day of Summmer",
    "poem" : """Beautiful sunrise
                On a warm summer morning.
                I wait for day's start."""
}
haikus = [haiku1, haiku2, haiku3]


def make_haiku_page(haiku):
    html = """<!DOCTYPE html>
    <html lang="en>

        <head>
        <meta charset ="UTF-8">
        <title>%s</title>
        </head>
        
        <body>
           <h1>%s</h1>
           <p>%s</p>
        </body>
    <html>""" % (haiku["title"],haiku["title"],haiku["poem"])

    f = open(haiku["title"] + ".html", "w")
    f.write(html)
    f.close()


def poem_links(haikus2):
    list_code=""
    for haiku in haikus2:
        list_code += """<li><a href="%s.html">%s</a></li>""" % (haiku["title"],haiku["title"])
    return list_code




def make_main_page():
    html = """<!DOCTYPE html>
    <html lang="en>

        <head>
        <meta charset ="UTF-8">
        <title>List of Haiku Poems</title>
        </head>
        
        <body>
            <h1>List of Haikus</h1>
            <ul>
                %s
            </ul>
        </body>
    <html>""" % poem_links(haikus)

    f = open("main.html", "w")
    f.write(html)
    f.close()
make_main_page()
for haiku in haikus:
    make_haiku_page(haiku)
