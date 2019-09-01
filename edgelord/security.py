from . import security_data

class security:
    data = None

    def from_csv(self, file):
        self.data = security_data.security_data().from_csv(file)
        print(self.data)

        return self
