'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==1:
            return 0
        else:
            checklist=sorted(height)
            position0=height.index(checklist.pop())
            position1=height.index(checklist.pop())
            small=min(position0,position1)
            big=max(position0,position1)
            result=(big-small-1)*height[position1]
            while checklist:
                position=height.index(checklist.pop())
                if position < small:
                    result+=height[position]*(small-position-1)
                    small=position
                elif position >big:
                    result+=height[position]*(position-big-1)
                    big=position
                else:
                    result-=height[position]
            return result
The problem is I make no change to height and position could be the same
'''
'''
class Solution:
    def trap(self, height: List[int]) -> int:
      if len(height)==1:
            return 0
      else:
        height_dict = {index: value for index, value in enumerate(height)}
        # key:position value:value
        position0=max(height_dict, key=height_dict.get)
        del height_dict[position0]
        position1=max(height_dict, key=height_dict.get)
        del height_dict[position1]
        small=min(position0,position1)
        big=max(position0,position1)
        result=(big-small-1)*height[position1]
        while height_dict:
          position=max(height_dict, key=height_dict.get)
          del height_dict[position]
          if position < small:
            result+=height[position]*(small-position-1)
            small=position
          elif position >big:
            result+=height[position]*(position-big-1)
            big=position
          else:
            result-=height[position]
        return result

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==1:
            return 0
        else:
            checklist=sorted(height)
            position0=height.index(checklist.pop())
            height[position0]=-1
            position1=height.index(checklist.pop())
            small=min(position0,position1)
            big=max(position0,position1)
            result=abs(big-small-1)*height[position1]
            height[position1]=-1
            while checklist:
                position=height.index(checklist.pop())
                if position < small:
                    result+=height[position]*(small-position-1)
                    small=position
                elif position >big:
                    result+=height[position]*(position-big-1)
                    big=position
                else:
                    result-=height[position]
                height[position]=-1
            return result
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_height_left = height[left]
        max_height_right = height[right]
        water = 0
        while left < right:
            if max_height_left < max_height_right:
                left += 1
                if height[left] < max_height_left:
                    water += max_height_left - height[left]
                else:
                    max_height_left = height[left]
            else:
                right -= 1
                if height[right] < max_height_right:
                    water += max_height_right - height[right]
                else:
                    max_height_right = height[right]
        return water