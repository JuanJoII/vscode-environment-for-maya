import maya.cmds as cmds
import re


def rename_chain(
    chain_type='joint', increment_version=True, base_name='Leg_practice_L'
):
    '''
    Renombra los objetos seleccionados siguiendo la nomenclatura:
    {segment}_{base_name}_{type}_{version}

    chain_type: 'joint', 'IK', 'MAIN', 'ctrl' ...
    increment_version: True/False para subir el número
    base_name: parte central de la cadena (ej: 'Leg_practice_L')
    '''
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning('⚠️ Selecciona primero los joints u objetos a renombrar.')
        return

    version_pattern = re.compile(r'(\d+)$')

    for i, obj in enumerate(selection, 1):
        # Determinar el segmento por orden
        if i == 1:
            segment = 'upperLeg'
        elif i == 2:
            segment = 'middleLeg'
        else:
            segment = 'endLeg'

        # Obtener versión actual
        match = version_pattern.search(obj)
        current_version = int(match.group(1)) if match else 1

        if increment_version:
            current_version += 1

        new_name = f'{segment}_{base_name}_{chain_type}_{current_version:03d}'
        cmds.rename(obj, new_name)
        print(f'✅ {obj} → {new_name}')


# --- Ejemplo de uso directo ---
# Selecciona tus joints en Maya y luego ejecuta:
# rename_chain(chain_type='IK', increment_version=False, base_name='practice_L')
