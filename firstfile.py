import time


#装饰器
def timer(func):
  def inner(*args,**kwargs):
    star = time.time()
    res=func(*args,**kwargs)
    print(time.time()-star)
    return res
   return inner

@timmer
def run():
  time.sleep(1)
  print('..end')
  
if __name__ == '__main__':
  run()
