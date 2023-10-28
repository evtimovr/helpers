import csv
from collections import defaultdict

from jinja2 import Environment, FileSystemLoader


def parse_csv(csv_path):
    data = defaultdict(lambda: defaultdict(list))

    with open(csv_path) as f:
        reader = csv.DictReader(
            f,
            fieldnames=[
                'show', 'date', 'show_url', 'liar', 'party', 'minute', 'lie', 'context'
                'argumentation', 
            ],
            restkey='sources',
        )

        # discard the header row
        next(reader)

        for row in reader:
            row['sources'] = [item for item in row['sources'] if item]
            data[row['party']][row['liar']].append(row)

    return data


def render_template(data, output_path):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    num_party_lies = {
        party: sum(len(items) for items in liars.values())
        for party, liars in data.items()
    }

    for liars in data.values():
        index = 0
        for liar in sorted(liars.keys()):
            for item in liars[liar]:
                index += 1
                item['index'] = index

    with open(output_path, 'w') as f:
        f.write(template.render(data=data, num_party_lies=num_party_lies))


if __name__ == '__main__':
    data = parse_csv('input.csv')
    render_template(data, 'output.html')
