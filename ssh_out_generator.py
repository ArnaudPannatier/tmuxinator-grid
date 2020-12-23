from jinja2 import Environment, FileSystemLoader
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('n', type=int)
parser.add_argument('--w_per_line', type=int)
parser.add_argument('--template', type=str)


def main(args):
    file_loader = FileSystemLoader(".")
    env = Environment(loader=file_loader)
    template = env.get_template(args.template)
    s = args.w_per_line**2
    windows = [
        {
            "title": "window{}".format(window),
            "panes": [i+1 for i in range(s)]
        } for window in list(range(args.n // s))]
    if args.n % s:
        windows.append({
            "title": "window{}".format(args.n // s + 1),
            "panes": [{"name": str(i+1)} for i in range(args.n % s)]})
    print(template.render(windows=windows))


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
