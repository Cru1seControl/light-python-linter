import argparse
import timeit
import sys

#argument setup
argsparse = argparse.ArgumentParser()

argsparse.add_argument("-fd", help="File descriptor to compile", type=str)

argsparse.add_argument("--string", help="Execute python code from string", type=str)
argsparse.add_argument("--silent", help="Don't raise exception when encountering an error", action="store_true")

args = argsparse.parse_args()

start = timeit.default_timer()

#check for syntax mistakes or general errors
def syntax_check():
    errors = 0
    try:
        if args.string:
            print(sys.version.replace("\n", ""), "\n") #version-ing

            if ";" in args.string: #check for newline in string
                code_arguments = args.string.split(";")
                for all_code in code_arguments:
                    all_code = all_code.strip()
                    exec(all_code)
            else:
                exec(args.string)

    except Exception as str_error:
        errors += 1
        print("[+] String compiled with %s errors" % (errors))
        if args.silent:
            pass
        else:
            print(str_error)

    if args.fd: #run each line of code from a file seprate to check for errors
        print(sys.version.replace("\n", ""), "\n")
        with open(args.fd, "r") as code_to_compile:
            python_code = code_to_compile.read().split("\n")

        try:
            for code in python_code:
                 try:
                     exec(code) #execute that fd code

                 except Exception as e:

                     errors += 1
                     if args.silent:
                         pass
                     else:
                         print(e)
                         pass

        except Exception as synerror:
            print("[+] %s compiled with %s errors" % (args.fd, errors))
            if args.silent:
                pass
            else:
                print(synerror)
                pass

    print("[+] Code executed in %s" % (timeit.default_timer() - start))

syntax_check()
