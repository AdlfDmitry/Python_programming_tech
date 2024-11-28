def makeLog(a, operation, b, result, log_file="log.txt"):
    try:
        f = open(log_file, "a")
        log_entry = f"{a=}, {operation=}, {b=}, {result=}\n"
        f.write(log_entry)
        f.close() 
    except Exception as e:
        print(f"Error writing to log file: {e}")
