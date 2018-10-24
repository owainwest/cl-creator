from subprocess import call
import pathlib

if __name__ == '__main__':
    template = input('CL template location: ')
    
    while True:
        company = input('company: ')
        role = input('role: ')

        with open(template, 'r') as f:
            text = f.read()

        text = text.replace('ROLE', role)
        text = text.replace('COMPANY', company)

        pathlib.Path('./CLs/{0}'.format(company)).mkdir(parents=True, exist_ok=True)

        cl_fname = 'cl-{0}-{1}.tex'.format(company.lower(), role.lower())
        cl_loc = './CLs/{0}/{1}'.format(company, cl_fname)

        with open(cl_loc, 'w') as f:
            f.write(text)

        call(["pdflatex", '-output-directory', './CLs/{0}/'.format(company), cl_loc])

        cont = input('Press y to make more, anything else to exit: ')
        if cont != 'y':
            break