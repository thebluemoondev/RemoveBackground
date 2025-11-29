from withoutbg import WithoutBG

INPUT_IMAGE = ''  #<-- name_image_need_remove_bg
OUTPUT_IMAGE = '' #<-- result

remover = WithoutBG.opensource()
result = remover.remove_background(INPUT_IMAGE)
result.save(OUTPUT_IMAGE)