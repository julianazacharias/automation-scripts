from fpdf import FPDF 

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('tiger.jpeg', w=80, h=50)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Malayan Tiger", align='C', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt='Description', ln=1)

pdf.set_font(family='Times', size=12)

txt1 = """Mussum Ipsum, cacilds vidis litro abertis. Não sou faixa preta cumpadi, 
sou preto inteiris, inteiris. Nulla id gravida magna, ut semper sapien. Vehicula non. 
Ut sed ex eros. Vivamus sit amet nibh non tellus tristique interdum. Si num tem leite então bota uma pinga aí cumpadi!

Atirei o pau no gatis, per gatis num morreus. Manduma pindureta quium dia nois paga. 
Vehicula non. Ut sed ex eros. Vivamus sit amet nibh non tellus tristique interdum. 
Nullam volutpat risus nec leo commodo, ut interdum diam laoreet. Sed non consequat odio.

Cevadis im ampola pa arma uma pindureta. Detraxit consequat et quo num tendi nada. 
Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis. 
Admodum accumsan disputationi eu sit. Vide electram sadipscing et per."""

pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Kingdom:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Phylum:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Chordata', ln=1)


pdf.output('output.pdf')