from communicationApp import createClient
def main():

  telegram = createClient('Line', bot_token ='1632387033:AAEgUxJiAwZBRVXwVpocXohQOxZYFhkkR6g')
  result = telegram.send_message("hi")
  print("---------end")
  print(result)

if __name__ == '__main__':
  try:
      main()
  except KeyboardInterrupt:
      exit()