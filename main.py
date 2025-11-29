from withoutbg import WithoutBG

INPUT_IMAGE = ''
OUTPUT_IMAGE = ''

remover = WithoutBG.opensource()
result = remover.remove_background(INPUT_IMAGE)
result.save(OUTPUT_IMAGE)