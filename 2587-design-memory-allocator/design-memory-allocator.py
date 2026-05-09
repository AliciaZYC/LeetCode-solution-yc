class Allocator:
    def __init__(self, n: int):
        self.memory_arr = [0] * n  # Track memory state: 0=free, mID=allocated
        self.memory_id_to_locations = {}  # Unused in current implementation
        self.free_list = []  # Unused in current implementation

    def allocate(self, size: int, mID: int) -> int:
        start_idx = 0  # Start of current free block
        for end_idx, byte in enumerate(self.memory_arr):
            curr_block = end_idx - start_idx + 1  # Current consecutive free count
            
            if byte != 0:  # Found occupied memory
                start_idx = end_idx + 1  # Reset start to next position
            elif curr_block >= size:  # Found large enough free block
                # BUG: This allocates curr_block units, not size units!
                self.memory_arr[start_idx:end_idx+1] = [mID] * curr_block
                return start_idx
        return -1  # No suitable block found

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i, byte in enumerate(self.memory_arr):  # O(n) scan
            if byte == mID:
                count += 1
                self.memory_arr[i] = 0  # Free the memory
        return count