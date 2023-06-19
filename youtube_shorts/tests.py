from video_generator import VideoGenerator

from colorama import init, Fore
init(autoreset=True)


test_count = 0


def check_passed(func):
    function_name = func.__name__.upper().replace("_", " ")

    def wrapper():
        global test_count

        try:
            func()
        except Exception as error:
            print(error)
            print(f"{Fore.RED} [{test_count}] [{function_name}] TEST NOT PASSED!")
        else:
            print(f"{Fore.GREEN} [{test_count}] [{function_name}] TEST HAS PASSED!")
        finally:
            test_count += 1

    return wrapper


def tests():
    test_video_generator()


@check_passed
def test_video_generator():
    next(VideoGenerator())


if __name__ == '__main__':
    tests()
