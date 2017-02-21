import random

class IpsumGenerator:

    word_list = [
        'Duis', 'Proin', 'faucibus,', 'Pellentesque', 'at', 'lectus', 'fermentum', 'vel.', 'justo,', 'metus',
        'ultricies', 'mattis', 'mauris', 'mi.', 'facilisi.', 'Curabitur', 'sem', 'congue.', 'nibh,', 'dui', 'dolor',
        'molestie', 'gravida', 'sit', 'auctor', 'ut.', 'condimentum', 'Vestibulum', 'lacinia', 'consectetur.',
        'commodo,', 'massa', 'nulla', 'feugiat', 'convallis,', 'euismod', 'nibh.', 'nisl,', 'vel', 'congue', 'commodo',
        'velit.', 'turpis', 'nisl', 'dignissim', 'porta', 'Praesent', 'eget,', 'enim', 'ante.', 'iaculis.', 'neque',
        'velit', 'ante', 'hendrerit,', 'Ut', 'metus,', 'blandit', 'convallis', 'mollis', 'pulvinar', 'rutrum', 'Fusce',
        'tempor.', 'risus,', 'malesuada.', 'elit.', 'efficitur', 'urna', 'leo', 'dui.', 'elit', 'Morbi', 'consequat',
        'eros', 'quam.', 'nec', 'sed', 'facilisis', 'fringilla.', 'pellentesque', 'Nullam', 'eleifend', 'tincidunt,',
        'lacus', 'adipiscing', 'Suspendisse', 'in', 'lorem', 'et.', 'purus,', 'commodo.', 'placerat', 'egestas',
        'tempor', 'sollicitudin,', 'cursus', 'nulla.', 'Integer', 'porttitor', 'eu.', 'volutpat,', 'Cras',
        'consectetur', 'augue', 'primis', 'ex', 'posuere', 'laoreet.', 'Etiam', 'interdum', 'ut', 'Sed', 'urna.',
        'mi', 'a,', 'erat.', 'lorem.', 'neque.', 'Donec', 'tellus,', 'Phasellus', 'eget', 'cubilia', 'volutpat',
        'libero', 'rutrum,', 'mauris.', 'sodales', 'elit,', 'viverra', 'neque,', 'vitae,', 'felis', 'risus.', 'magna',
        'Quisque', 'felis,', 'sed.', 'pretium', 'sem.', 'mi,', 'aliquet.', 'scelerisque', 'hendrerit', 'faucibus',
        'Nulla', 'vulputate', 'lobortis', 'nulla,', 'viverra.', 'libero.', 'lobortis,', 'nec,', 'enim,', 'augue.',
        'Nam', 'ullamcorper', 'erat', 'sollicitudin', 'tincidunt', 'ac', 'Maecenas', 'molestie,', 'varius', 'lacus.',
        'orci', 'bibendum', 'pharetra', 'maximus', 'risus', 'lobortis.', 'Aenean', 'malesuada', 'tortor.', 'purus',
        'luctus', 'nisi', 'tellus.', 'Vivamus', 'pellentesque.', 'in,', 'Lorem', 'quis', 'amet,', 'a', 'tellus', 'id',
        'In', 'aliquet', 'justo', 'ligula.', 'cursus.', 'et', 'fringilla', 'eleifend,', 'vehicula', 'ipsum',
        'condimentum.', 'eu', 'ante,', 'non', 'suscipit', 'massa,', 'interdum,', 'iaculis', 'nibh', 'faucibus.', 'leo.',
        'auctor,', 'vitae', 'arcu.', 'vestibulum', 'varius.', 'diam,', 'ligula', 'tristique', 'in.', 'tortor', 'quam',
        'finibus.', 'arcu', 'Mauris', 'semper.', 'sapien', 'sagittis', 'dapibus', 'vulputate,', 'Aliquam', 'id.',
        'ultrices', 'Curae;', 'est', 'laoreet', 'amet', 'quis,', 'lectus.', 'rhoncus', 'accumsan', 'quam,', 'est.'
    ]

    def __init__(self, paragraph_count, word_count):
        if paragraph_count == 0 or word_count == 0:
            raise Exception("Cannot provide zero paragraphs or zero words")
            
        self.paragraph_count = paragraph_count
        self.word_count = word_count
        self.words_per_paragraph = self.word_count / self.paragraph_count
        self.additional_words = self.word_count % self.paragraph_count

    def generate_paragraphs(self):

        text = ''
        paragraphs_processed = 1

        while paragraphs_processed <= self.paragraph_count:
            paragraphs_processed += 1
            words_in_paragraph = 1

            if paragraphs_processed == self.paragraph_count:
                words_in_paragraph -= self.additional_words

            paragraph = '<p>'

            while words_in_paragraph <= self.words_per_paragraph:
                words_in_paragraph += 1
                paragraph += random.choice(self.word_list) + ' '

            paragraph += '</p>'

            text += paragraph

        return text
