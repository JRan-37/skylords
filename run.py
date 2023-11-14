import sys
import importlib.util

if __name__ == "__main__":
    argv = sys.argv
    port = 7079
    if len(argv) > 3 or len(argv) < 2:
        print("Invalid arguments! " +
              "First argument should be the path to the bot implementation, " +
              "second argument the port to run it on (default: 7079).")
        quit()
    elif len(argv) == 2:
        print("No port was specified. Using default port 7079.")
    else:
        port = int(argv[2])

    botpath = argv[1]
    modparent = botpath.split('/')[-2]
    botname = botpath.split('/')[-1][:-3]
    modulename = modparent + "." + botname

    spec = importlib.util.spec_from_file_location(modulename, botpath)
    b = importlib.util.module_from_spec(spec)
    sys.modules[modulename] = b
    spec.loader.exec_module(b)

    b.main(port)
