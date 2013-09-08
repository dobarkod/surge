from subprocess import check_output
import json

def run_test(concurrency, duration):
    out = check_output(['./python/test-runner',
        str(concurrency), str(duration)])
    return json.loads(out)
