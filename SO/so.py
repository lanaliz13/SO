import random

def page_reference(length, num_pages):
    return [random.randint(0, num_pages - 1) for _ in range(length)]

def fifo(pages, frame_count):
    frames = []
    page_faults = 0

    for page in pages:
        if page not in frames:
            if len(frames) >= frame_count:
                frames.pop(0)  # Remove o primeiro (FIFO)
            frames.append(page)
            page_faults += 1

    return page_faults

def lru(pages, frame_count):
    frames = []
    page_faults = 0

    for page in pages:
        if page not in frames:
            if len(frames) >= frame_count:
             
                lru_page = frames.pop(0)
                frames.append(page)
            else:
                frames.append(page)
            page_faults += 1
        else:
            
            frames.remove(page)
            frames.append(page)

    return page_faults

def teste(pstring, frame_counts):
    for frame_count in frame_counts:
        fifo_faults = fifo(pstring, frame_count)
        lru_faults = lru(pstring, frame_count)
        print(f"Frames: {frame_count} | FIFO faults: {fifo_faults} | LRU faults: {lru_faults}")


num_pages = 10
string_length = 20
frame_counts = [3, 4, 5] 


pstring = page_reference(string_length, num_pages)
print("Page Reference String:", pstring)


teste(pstring, frame_counts)