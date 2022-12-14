def ge(good_ending_pages, bad_ending_pages, page_option):
    good_ending_pages = set(good_ending_pages)
    bad_ending_pages = set(bad_ending_pages)
    
    page_option_map = {}
    for option in page_option:
        page_option_map[option[0]] = option[1:]
    
    res = set()
    visited = set()
    
    def dfs(page_no):
        # exit: 走到坏的或是进了loop
        if page_no in bad_ending_pages or page_no in visited: return
        visited.add(page_no)
        
        if page_no in good_ending_pages:
            res.add(page_no)
            good_ending_pages.remove(page_no)
        elif page_no not in page_option_map:
            dfs(page_no + 1)
        else: 
            for option in page_option_map[page_no]:
                dfs(option)

    dfs(1)
    return res
