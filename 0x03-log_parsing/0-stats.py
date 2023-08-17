#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
if __name__ == "__main__":
    import sys
    sta_code = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    total_file = 0
    lines_processed = 0
    
        
    try:
        for line in sys.stdin:
            num = line.split()
            if len(num) > 4:
                getStatus = num[-2]
                if getStatus in sta_code.keys():
                    sta_code[getStatus] += 1
                total_file = total_file + int(num[-1])
                lines_processed += 1
            if lines_processed == 10:
               lines_processed = 0
               print("File size: {}".format(total_file))
               for key, value in sorted(sta_code.items()):
                if value:
                    print(f"{key}: {value}") 
    except Exception as err:
        pass
    finally:
        print("File size: {}".format(total_file))
        for key, value in sorted(sta_code.items()):
            if value:
                print(f"{key}: {value}")

