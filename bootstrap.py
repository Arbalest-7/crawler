from parser.unqiueUgc import unqiueUgc

rawFile = '/Users/dainping/PycharmProjects/reptile/resources/mawu_raw_ugc.txt'
dstFile = "/Users/dainping/PycharmProjects/reptile/resources/mawu_unqiue_ugc.txt"


if __name__ == '__main__':
    # main.download.downloadAndSave.save_to_txt()
   unqiueUgc(rawFile, dstFile)
   print("task finish")
