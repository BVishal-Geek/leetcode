class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0  # Start of window
        w_count = blocks[:k].count("W")  # Count 'W' in first k characters
        min_w = w_count  # Initialize min replacements
        
        for right in range(k, len(blocks)):  # Expand window
            if blocks[right] == "W":
                w_count += 1  # Add new W
            if blocks[left] == "W":
                w_count -= 1  # Remove old W
            left += 1  # Move window forward
            
            min_w = min(min_w, w_count)  # Update min W recolors
        
        return min_w