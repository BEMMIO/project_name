from celery import shared_task


@shared_task(bind=True)
def test_func(*args,**kwargs):
	user_name = kwargs.get("username")
	print(user_name)
	for i in range(20):
		print("CounterB for {1}".format(i,user_name))
	return "Successfully executed."
