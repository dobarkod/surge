from redis import Redis
from rq import Queue
from math import sqrt

q = Queue(connection=Redis())

jr = q.enqueue('worker.run_test', 5, 1)

import time

while jr.result is None:
    time.sleep(1)

duration = jr.result['duration']
results = jr.result['results']


print "Requests:", len(results)
succ = [r['duration'] for r in results if r['success']]
err = [r['error_details'] for r in results if not r['success']]

print "Successes:", len(succ)
print "Errors:", len(err)

if len(succ) > 10:
    a = sum(succ) / len(succ)
    r_avg = int(1000.0 * a)
    r_min = int(1000.0 * min(succ))
    r_max = int(1000.0 * max(succ))
    r_dev = sqrt(sum((r - a) * (r - a) for r in succ) / (len(succ) - 1))
    print "Average: %d ms" % r_avg
    print "Minimum: %d ms" % r_min
    print "Maximum: %d ms" % r_max
    print "Std.dev: %.2f" % r_dev
    print "Runtime: %.2f s" % duration
    print "Reqs/s: %d" % int(len(succ) / duration)

if err:
    print "Errors:", len(err)
    # for e in err:
    #    print "  - " + e
