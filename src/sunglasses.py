import inspect
import sys
import config


def show_usage():
    print "Usage: %s log_file" % sys.argv[0]


if len(sys.argv) < 1:
    show_usage()
    sys.exit(1)


log_file = sys.argv[1]
filters = config.FILTER_MODULES

for module_name in config.FILTER_MODULES:
    filters_module = __import__(module_name)
    for name in dir(filters_module):
        if name.startswith('__'):
            continue
        elif name == 'LogFilter':
            continue

    klass = getattr(filters_module, name)
    if inspect.isclass(klass) and issubclass(klass, filters_module.LogFilter):
        #print 'add %s into filter' % klass
        filters.append(klass())

