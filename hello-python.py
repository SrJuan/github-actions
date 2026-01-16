import os

def main():
  nameUser = os.getenv('USERNAME', 'user')
  print(f"Hola {nameUser} from github")

if __name__ == "__main__":
  main()
