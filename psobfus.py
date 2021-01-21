import base64
from argparse import ArgumentParser

class Obfuscator:
    '''
    Powershell code obfuscator
    '''
    def __init__(self ,file):
        self.file = file
        self.payload = '([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("{}")))'

    def check_file(self):
        file_extension = self.file.split('.')[-1]
        if file_extension != 'ps1':
            print('Error : file extension must be .ps1')
            exit()

    def obfuscate(self):
        try:
            with open(self.file ,'r') as file :
                ps_file_content = file.read()
        except FileNotFoundError :
            print(f'Error : file ({self.file}) does not exist')
            exit()

        content_bytes = ps_file_content.encode('UTF-8')
        base64_bytes = base64.b64encode(content_bytes)
        base64_msg = base64_bytes.decode('UTF8')

        injected_payload = self.payload.format(base64_msg)
        final_payload = 'iex ' + injected_payload

        new_file_name = self.file.split('.')[0] + '_obfuscated.ps1'
        with open(new_file_name ,'w') as new_file :
            new_file.write(final_payload)

        print('Powershell code obfuscated successfully.')
        print('Obfuscated file --> ' + new_file_name)


def print_help():
    help_msg = '''
usage: psobfus.py [--file (powershell file name or path)]

optional arguments:
  --file ,-file ,-f (powershell file name or path e.g : myscript.ps1)
    '''
    print(help_msg)

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--file','-file','-f' ,metavar='(powershell file name or path)')
    args ,unknown = parser.parse_known_args()
    if (args.file is not None) :
        obfuscator = Obfuscator(file=args.file)
        obfuscator.check_file()
        obfuscator.obfuscate()
    else:
        print_help()

