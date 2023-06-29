import utils
import commands as cmd
import chatbot


def run():
    exit_conditions = ("q", "quit", "exit", "stop")

    while True:
        command = utils.listen().lower()
        if command in exit_conditions:
            break

        elif command == 'hello':
            cmd.greet()

        elif 'time' in command:
            cmd.current_time()

        elif 'wiki' in command:
            cmd.wiki(command)

        elif 'google' in command:
            cmd.google(command)

        elif 'youtube' in command:
            cmd.youtube(command)

        elif 'mail' in command:
            cmd.mail()

        else:
            response = chatbot.respond(command)
            utils.speak(response)

        # utils.speak(command)


def output_result():
    ...


if __name__ == '__main__':
    run()
