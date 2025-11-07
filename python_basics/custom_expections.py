





class ListHasBError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


def trigger_error(let: str, lst: list):
    if let in lst:
        print("Inside the fuction")
        raise ListHasBError("List has B! WARNING!")


lst = ["a", "c", "b"]
let = "b"

try:
    trigger_error(let, lst)
except ListHasBError as e:
    print(f"Error triggered: {e}")
finally:
    print("We are done here")
