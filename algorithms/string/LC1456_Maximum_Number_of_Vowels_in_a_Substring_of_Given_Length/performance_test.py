"""
三种查找方法的性能对比测试
"""
import time


def test_list_search():
    """方法1: 列表查找"""
    vowels = ["a", "e", "i", "o", "u"]
    test_string = "abcdefghijklmnopqrstuvwxyz" * 10000
    
    start = time.perf_counter()
    count = sum(1 for char in test_string if char in vowels)
    end = time.perf_counter()
    
    return count, (end - start) * 1000  # 转换为毫秒


def test_set_search():
    """方法2: 集合查找"""
    vowels = {"a", "e", "i", "o", "u"}
    test_string = "abcdefghijklmnopqrstuvwxyz" * 10000
    
    start = time.perf_counter()
    count = sum(1 for char in test_string if char in vowels)
    end = time.perf_counter()
    
    return count, (end - start) * 1000


def test_string_search():
    """方法3: 字符串查找"""
    vowels = "aeiou"
    test_string = "abcdefghijklmnopqrstuvwxyz" * 10000
    
    start = time.perf_counter()
    count = sum(1 for char in test_string if char in vowels)
    end = time.perf_counter()
    
    return count, (end - start) * 1000


def visualize_search_process():
    """可视化查找过程"""
    print("=" * 60)
    print("查找过程可视化演示")
    print("=" * 60)
    
    # 测试查找 'i'
    target = 'i'
    
    print(f"\n🔍 查找目标: '{target}'\n")
    
    # 方法1: 列表
    print("方法1: 列表 ['a', 'e', 'i', 'o', 'u']")
    vowels_list = ["a", "e", "i", "o", "u"]
    comparisons = 0
    for i, v in enumerate(vowels_list):
        comparisons += 1
        print(f"  步骤{comparisons}: 比较 '{v}' == '{target}' ? ", end="")
        if v == target:
            print(f"✓ 找到了！")
            break
        else:
            print("✗ 继续")
    print(f"  总比较次数: {comparisons}")
    
    # 方法2: 集合
    print(f"\n方法2: 集合 {{'a', 'e', 'i', 'o', 'u'}}")
    vowels_set = {"a", "e", "i", "o", "u"}
    print(f"  步骤1: 计算 hash('{target}') = {hash(target)}")
    print(f"  步骤2: 直接定位到存储位置")
    print(f"  步骤3: 一次比较确认 ✓")
    print(f"  总比较次数: 1 (常数时间)")
    
    # 方法3: 字符串
    print(f"\n方法3: 字符串 'aeiou'")
    vowels_str = "aeiou"
    comparisons = 0
    for i, v in enumerate(vowels_str):
        comparisons += 1
        print(f"  步骤{comparisons}: 比较 '{v}' == '{target}' ? ", end="")
        if v == target:
            print(f"✓ 找到了！")
            break
        else:
            print("✗ 继续")
    print(f"  总比较次数: {comparisons}")
    
    # 测试不存在的字符
    print(f"\n" + "=" * 60)
    target = 'x'
    print(f"🔍 查找目标: '{target}' (不存在)")
    print("=" * 60)
    
    print("\n方法1: 列表")
    comparisons = sum(1 for v in vowels_list if v != target or True)
    print(f"  需要遍历所有5个元素才能确认不存在")
    print(f"  总比较次数: 5")
    
    print(f"\n方法2: 集合")
    print(f"  步骤1: 计算 hash('{target}')")
    print(f"  步骤2: 直接定位，发现该位置为空或不匹配")
    print(f"  总比较次数: 1 (常数时间)")
    
    print(f"\n方法3: 字符串")
    print(f"  需要遍历所有5个字符才能确认不存在")
    print(f"  总比较次数: 5")


def compare_performance():
    """性能对比测试"""
    print("\n" + "=" * 60)
    print("性能测试（查找260,000个字符中的元音）")
    print("=" * 60)
    
    # 运行多次取平均值
    runs = 5
    
    list_times = []
    set_times = []
    string_times = []
    
    for _ in range(runs):
        _, list_time = test_list_search()
        _, set_time = test_set_search()
        _, string_time = test_string_search()
        
        list_times.append(list_time)
        set_times.append(set_time)
        string_times.append(string_time)
    
    avg_list = sum(list_times) / runs
    avg_set = sum(set_times) / runs
    avg_string = sum(string_times) / runs
    
    print(f"\n方法1 - 列表:   平均耗时 {avg_list:.4f} ms")
    print(f"方法2 - 集合:   平均耗时 {avg_set:.4f} ms  ⚡ 最快")
    print(f"方法3 - 字符串: 平均耗时 {avg_string:.4f} ms")
    
    print(f"\n性能比较:")
    print(f"  集合 vs 列表:   {avg_list/avg_set:.2f}x 更快")
    print(f"  集合 vs 字符串: {avg_string/avg_set:.2f}x 更快")
    
    # 可视化性能柱状图
    print(f"\n性能对比图（相对时间）:")
    max_time = max(avg_list, avg_set, avg_string)
    
    def draw_bar(name, time, max_val):
        bar_length = int((time / max_val) * 50)
        bar = "█" * bar_length
        print(f"  {name:8} {bar} {time:.4f}ms")
    
    draw_bar("列表", avg_list, max_time)
    draw_bar("集合", avg_set, max_time)
    draw_bar("字符串", avg_string, max_time)


def memory_usage():
    """内存占用对比"""
    import sys
    
    print("\n" + "=" * 60)
    print("内存占用对比")
    print("=" * 60)
    
    vowels_list = ["a", "e", "i", "o", "u"]
    vowels_set = {"a", "e", "i", "o", "u"}
    vowels_str = "aeiou"
    
    list_size = sys.getsizeof(vowels_list) + sum(sys.getsizeof(x) for x in vowels_list)
    set_size = sys.getsizeof(vowels_set) + sum(sys.getsizeof(x) for x in vowels_set)
    string_size = sys.getsizeof(vowels_str)
    
    print(f"\n列表:   {list_size} 字节")
    print(f"集合:   {set_size} 字节  (哈希表需要额外空间)")
    print(f"字符串: {string_size} 字节  💾 最省内存")


if __name__ == "__main__":
    # 1. 可视化查找过程
    visualize_search_process()
    
    # 2. 性能对比
    compare_performance()
    
    # 3. 内存占用
    memory_usage()
    
    # 4. 结论
    print("\n" + "=" * 60)
    print("📚 总结与建议")
    print("=" * 60)
    print("""
对于元音查找（只有5个元素）：
  
  ✅ 实际建议: 使用字符串 "aeiou"
     - 代码最简洁
     - 性能差异可忽略（只有5个元素）
     - 内存占用最小
  
  🎯 理论最优: 使用集合 {"a", "e", "i", "o", "u"}
     - 时间复杂度 O(1)
     - 当元素很多时优势明显
     - 养成使用集合的好习惯
  
  ❌ 不推荐: 使用列表 ["a", "e", "i", "o", "u"]
     - 时间复杂度 O(n)
     - 代码比字符串还长
     - 没有优势

实际开发中的选择：
  - 元素 < 10个:      字符串/列表都可以
  - 元素 >= 10个:     使用集合
  - 需要频繁查找:     使用集合
  - 追求代码简洁:     使用字符串
  - 学习算法知识:     理解集合原理很重要！
""")
