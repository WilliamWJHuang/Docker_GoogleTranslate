import click
import googletrans

@click.command()
def GoTranslate():
    text = input("Please enter the words/sentences you would like to translate: ")
    translator = googletrans.Translator()
    translated = translator.translate(text)
    print(translated.text)

if __name__ == '__main__':
    GoTranslate()
