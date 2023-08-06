import click
import requests
import json

URL = "https://cybersecurity-club-324422.appspot.com"

@click.group()
def triex():
    """This application is a CLI that connects to a remote trie server stored on Google Cloud"""
    pass

@click.command(help="Displays all words stored inside the trie")
def display():
    try:
      r = requests.get(URL + "/display")
      trie = json.loads(r.text)["trie"]
      if len(trie) == 0:
          print("The trie is empty! Feel free to add words to it using the insert function!")
      else:
        prompt = "Here are all the words inside the trie"
        click.echo(prompt)
        click.echo("-"*len(prompt))
        for word in trie:
            click.echo(word)
    except:
        click.echo("An error occurred while trying to display the trie")

@click.command(help="Inserts a word into the trie")
@click.option('--word','-w', help='Word to be inserted into the trie',prompt='What word do you want to insert',type=str)
def insert(word):
    try:
      r = requests.post(URL + "/insert", json={"word": word})
      res = json.loads(r.text)
      if res["insert"] == "success":
          click.echo("Word inserted successfully")
    except:
        click.echo("An unexpected error occurred. Please verify that your word does not already exist in the trie.")

@click.command(help="Deletes a word from the trie")
@click.option('--word','-w', help='Word to be deleted from the trie',prompt='What word do you want to delete',type=str)
def delete(word):
    try:
      r = requests.post(URL + "/delete", json={"word": word})
      res = json.loads(r.text)
      if res["delete"] == "success":
          click.echo("Word deleted successfully")
    except:
        click.echo("An unexpected error occurred. Please verify that your word exists in the trie.")

@click.command(help="Checks whether a word exists in the trie")
@click.option('--word','-w', help='Word to be checked',prompt='What word do you want to find in the trie',type=str)
def search(word):
    try:
      r = requests.get(URL + f"/search?word={word}")
      res = json.loads(r.text)["found"]
      if res:
          click.echo("Word successfully found in the trie")
      elif res == False:
          click.echo("Word not found in the trie")
    except:
        click.echo("An error occured while searching for your word.")

@click.command(help="Gives autocomplete suggestions based on a given prefix")
@click.option('--prefix','-p', help='Prefix used to calculate suggestions',prompt='What word do you want to use as a prefix',type=str)
def autocomplete(prefix):
    try:
      r = requests.get(URL + f"/autocomplete?prefix={prefix}")
      res = json.loads(r.text)["suggestions"]
      if len(res)>0:
          prompt = f"Here are the suggestions based on the prefix of {prefix}"
          click.echo(prompt)
          click.echo("-"*len(prompt))
          for i in res:
              click.echo(i)
      else:
          click.echo("No suggestions found")
    except:
        click.echo("An error occured while trying to find autocomplete suggestions for your word.")

triex.add_command(display)
triex.add_command(insert)
triex.add_command(delete)
triex.add_command(search)
triex.add_command(autocomplete)


if __name__ == '__main__':
    triex()