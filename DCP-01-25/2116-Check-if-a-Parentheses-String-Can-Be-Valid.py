class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False  # Odd-length strings cannot form valid parentheses
        
        # Left-to-right pass
        open_count = 0
        flexible_count = 0
        for i in range(n):
            if locked[i] == '0':  # Flexible position
                flexible_count += 1
            elif s[i] == '(':
                open_count += 1
            else:  # s[i] == ')'
                if open_count > 0:  # Match with a previous '('
                    open_count -= 1
                elif flexible_count > 0:  # Use a flexible position as '('
                    flexible_count -= 1
                else:
                    return False  # No match possible
        
        # Right-to-left pass
        close_count = 0
        flexible_count = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':  # Flexible position
                flexible_count += 1
            elif s[i] == ')':
                close_count += 1
            else:  # s[i] == '('
                if close_count > 0:  # Match with a previous ')'
                    close_count -= 1
                elif flexible_count > 0:  # Use a flexible position as ')'
                    flexible_count -= 1
                else:
                    return False  # No match possible
        
        return True
