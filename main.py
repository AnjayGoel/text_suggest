import keyboard
import suggest

count = 0
word = ""
prev = ''
once = False
suggestions = []
requested = 3
returned = 0
wait = 0


def callback(event):
    global count
    global word
    global once
    global returned
    global requested
    global suggestions
    global wait
    if not wait == 0:
        print('waiting')
        wait -= 1
        return
    if event.event_type == keyboard.KEY_UP and event.name == 'alt':
        keyboard.unhook_all()
        keyboard.unhook(callback)
        if count == 0 and not once:

            suggestions = suggest.suggest(word, requested)
            suggestions.append(word)
            returned = len(suggestions)
            print("word: " + word + " suggestions:", end=' ')
            print(suggestions)
            print('count is 0')

            count += 1
            word = ''
            for i in range(len(suggestions[returned - 1])):
                wait += 1
                keyboard.send('backspace')
            wait += len(suggestions[0])
            word=suggestions[0]
            keyboard.write(suggestions[0])

        else:
            for i in range(len(suggestions[count - 1])):
                keyboard.send('backspace')
                wait += 1
            word = ''
            keyboard.write(suggestions[count])
            wait += len(suggestions[count])
            word = suggestions[count]
            count += 1
            if count == returned:
                once = True
            count %= returned
        keyboard.hook(callback)

    if event.event_type == keyboard.KEY_DOWN:
        if len(event.name) == 1 and 97 <= ord(event.name) <= 122:
            word = word + event.name

        if event.name == 'space' or event.name == 'enter':
            print('space or enter')
            count = 0
            word = ''
            suggestions = []
            once = False
        if event.name == 'backspace':
            print('bs')
            word = word[:-1]
            print(word)

keyboard.hook(callback)
keyboard.wait()
