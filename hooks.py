import os.path
import posixpath

def on_pre_page(page, config, files):
    print('on pre page %s, %s' % (page, page.file))
    #new_ext = '.html'
    #file = page.file
    #file.dest_path = os.path.splitext(file.dest_path)[0] + new_ext
    #file.abs_dest_path = os.path.splitext(file.abs_dest_path)[0] + new_ext
    if page.file.url.endswith('/')
         file.url += page.file.url
    #if file.url.endswith('/'):
    #    file.url += 'index' + new_ext
    #else:
    #    file.url = posixpath.splitext(file.url)[0] + new_ext