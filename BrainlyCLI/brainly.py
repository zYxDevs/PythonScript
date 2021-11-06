from brainly_scraper import brainly

cyan  = '\x1b[36m'
white = '\x1b[37m'

def start():
    banners = """
{} ____            _       _       
| __ ) _ __ __ _(_)_ __ | |_   _ 
|  _ \| '__/ _` | | '_ \| | | | |
| |_) | | | (_| | | | | | | |_| |
|____/|_|  \__,_|_|_| |_|_|\__, | {}Made By zYxDevs
{}                           |___/  {}Brainly-CLI V1
""".format(cyan, white, cyan, white)
    print(banners)

if __name__=='__main__':
    start()
    while True:
        try:
            tanya = input('{}Masukan Pertanyaan: {}'.format(cyan, white))
            scrap = brainly(tanya, 5)
            for i in scrap:
                for answer in i.answers:
                    print('{}'.format(white)+answer.content + '{}\n\n----------------------\n\n{}'.format(cyan, white, cyan))
        except KeyboardInterrupt:
            print('{}\nOke Byeee....'.format(cyan))
            exit()
