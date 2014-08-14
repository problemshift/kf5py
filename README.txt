===========
KF5 API
===========

An python package to access KF5 data via its API

    #!/usr/bin/env python

    from kf5py import kf5connection
    
    conn = kf5py.connection('http://localhost:8080/kforum/','username','password')
    print conn.is_valid()
    section_ids = conn.get_section_ids()
    views = conn.get_views_by_sectionid(section_ids[0])

    for view in views:
        viewjson = conn.get_view_by_viewid(view['guid'])
        for vpr in viewjson['viewPostRefs']:
            print vpr['location']