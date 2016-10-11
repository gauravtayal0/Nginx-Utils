import os 
import time

def process_log(lines):
    lined = []
    for line in lines:
        lined.append(line)
    print len(lined)
    return len(lined)

def build_source(access_log):
    begin = time.time()
    lines = follow(access_log,begin)
    return lines

# ======================
# generator utilities
# ======================
def follow(the_file,begin):
    """
    Follow a given file and yield new lines when they are available, like `tail -f`.
    """
    duration = 0
    with open(the_file) as f:
        f.seek(0, 2)  # seek to eof
        while duration < 1:
            line = f.readline()
            if not line:
                time.sleep(0.1)  # sleep briefly before trying again
                continue
            duration = time.time() - begin
            yield line


def process():
    access_log = '/var/log/nginx/access.log'

    #logging.info('access_log: %s', access_log)
    if not os.path.exists(access_log):
        error_exit('error log file "%s" does not exist' % access_log)

    source = build_source(access_log)
    process_log(source)

process()
