import dropbox
class Transferdata: 
    def __init__(self, accesstoken):
        self.accesstoken=accesstoken
    def uploadfile(self, source, destination):
        dbx= dropbox.Dropbox(self.accesstoken)
        f=open(source, 'rb')
        dbx.files_upload(f.read(), destination)
def main():
    accesstoken=''
    td=Transferdata(accesstoken)
    filefrom = input("Enter the path of the file to trsnsfer: ")
    fileto = input("Enter the path of the file to upload: ")
    td.uploadfile(filefrom, fileto)
    print("Files have been moved")
main()
