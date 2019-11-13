#!/usr/bin/python3

from argparse import ArgumentParser as Parser
from textanalyzer.dictionary import *
from sys import stderr, stdin, argv

def main():
    args = Parser(
        description = "A translater of codes, maked especialy for you porte the codes from some language to some language or convert simple texts.",
        prog = "Translater"
    )

    if not '-c' in argv and not '--config' in argv:
        args.add_argument( 'pattern', help = 'Short pattern to search in text.', type = str )
    args.add_argument( '-f', '--file', help = "File with the code to translation.", type = str)
    args.add_argument( '-c' , '--config', help = "Yaml with the dictionary for the translation.", type = str )
    args.add_argument( '-o', '--output', help = "File name where will write the output.", type = str )

    args = args.parse_args()

    config = args.config if args.config else '@c'+args.pattern

    file = File(args.file)

    output = File( args.output )
    translated = ''

    text = ''
    lang = Dictionary ( config )
    if args.file:
        text = lang.translate( file.text )
    else:
        text = lang.translate( stdin.read() )

    translated = lang.ident ( text, lang.config.properties[':identation'] )

    if output.filename:
        output.write( translated )

    print( translated )


if __name__=="__main__":
    main()
