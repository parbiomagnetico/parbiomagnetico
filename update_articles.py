import json

def update_posts():
    with open('src/data/posts.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)

    # Dictionary of new content
    new_content = {
        1: {
            "title": "¿Por qué el Equilibrio del pH es Vital para tu Salud? La Guía Definitiva",
            "excerpt": "Descubre la ciencia del pH interno y cómo el equilibrio ácido-base rige tu vitalidad. Aprende por qué el 'terreno biológico' es la clave de tu salud.",
            "content": """<!-- wp:paragraph -->
<p>Como especialista en salud bioenergética con años de práctica clínica, he observado una constante: el bienestar no es un estado estático, sino un <strong>equilibrio dinámico</strong>. Mantener una <strong>homeostasis</strong> interna correcta es fundamental para que nuestro organismo funcione al 100%. En mi consulta de <a href="/tratamientos">Par Biomagnético</a>, abordamos la salud desde una perspectiva integral, utilizando esta terapia complementaria para ayudar al cuerpo a recuperar su pH natural neutral (Nivel Energético Normal).</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>El Terreno Biológico: La Semilla vs. El Suelo</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Muchas veces nos enfocamos exclusivamente en los agentes externos —virus o bacterias— como si fueran los únicos villanos de nuestra salud. Sin embargo, la teoría del <strong>terreno biológico</strong> nos enseña que el 'microbio no es nada, el terreno lo es todo'. Si tu cuerpo mantiene un pH equilibrado (ligeramente alcalino en sangre, alrededor de 7.4), los patógenos no encuentran las condiciones necesarias para colonizarte. El equilibrio del pH es, en esencia, tu escudo biológico más potente.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>¿Qué es el pH y por qué una variación mínima importa tanto?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>El pH (Potencial de Hidrógeno) mide la concentración de iones de hidrógeno en una escala de 0 a 14. Al ser una escala logarítmica, un salto de 7 a 6 no es un punto de diferencia, sino que significa que la sustancia es <strong>diez veces más ácida</strong>. Tu cuerpo es una máquina de precisión:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
<li><strong>Sangre:</strong> Debe estar entre 7.35 y 7.45. Fuera de ahí, la vida peligra.</li>
<li><strong>Estómago:</strong> Debe ser ácido (1.5 - 3) para digerir y desinfectar.</li>
<li><strong>Piel:</strong> Mantiene un manto ácido protector.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h3>El robo de minerales: La trampa de la acidosis</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Cuando nuestro estilo de vida nos acidifica (estrés, mala dieta), el cuerpo activa los 'sistemas tampón'. Si estos fallan, el organismo recurre a una medida de supervivencia drástica: <strong>extrae minerales alcalinos</strong> (calcio, magnesio, potasio) de tus huesos y dientes para neutralizar la sangre. Este es el origen de la fatiga crónica y la descalcificación ósea.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Causas del desequilibrio en la vida moderna</h2>
<!-- /wp:heading -->

<p>Varios factores desplazan nuestro pH hacia el rango ácido:</p>

<!-- wp:list -->
<ul>
<li><strong>Estrés crónico:</strong> Altera la química interna y genera radicales libres rápidamente.</li>
<li><strong>Sedentarismo:</strong> La falta de oxigenación celular favorece la fermentación ácida.</li>
<li><strong>Alimentación Procesada:</strong> Dietas ricas en azúcares y harinas blancas rompen la homeostasis.</li>
<li><strong>Contaminación:</strong> Tanto química como electromagnética afecta nuestra polaridad celular.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Consecuencias de la Acidosis: Señales de alerta</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Un terreno biológico acidificado se manifiesta en síntomas que a veces normalizamos:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
<li><strong>Debilidad inmunitaria:</strong> Las defensas pierden movilidad y eficacia.</li>
<li><strong>Inflamación recurrente:</strong> El medio ácido es el combustible de la inflamación.</li>
<li><strong>Cansancio extremo:</strong> Sin el pH adecuado, las células no producen energía (ATP) de forma eficiente.</li>
<li><strong>Deterioro estructural:</strong> Problemas de cabello, uñas frágiles y calambres musculares.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Restauración con el Par Biomagnético</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>La terapia de <a href="/como-funciona">Par Biomagnético</a> actúa como un regulador natural. Mediante imanes de neodimio en <strong>puntos estratégicos</strong>, facilitamos la migración de iones y restablecemos la neutralidad de forma no invasiva. No solo aliviamos síntomas; estamos reparando el terreno para que la enfermedad no tenga donde esconderse.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>5 Consejos para mantener tu pH</h2>
<!-- /wp:heading -->

<ol>
<li><strong>Agua Alcalina:</strong> Un chorrito de limón en agua por la mañana (aunque es ácido, alcaliniza al metabolizarse).</li>
<li><strong>Respiración:</strong> Exhala profundamente para eliminar el exceso de CO2 (ácido volátil).</li>
<li><strong>Verduras Verdes:</strong> La clorofila es magnesio puro para tu pH.</li>
<li><strong>Descanso:</strong> El sueño reparador es el momento en que el cuerpo equilibra su química.</li>
<li><strong>Mente en Calma:</strong> Los pensamientos positivos generan una química alcalina.</li>
</ol>

<!-- wp:paragraph -->
<p>Mantener un pH equilibrado es la mejor garantía de salud a largo plazo. Si sientes que tu energía no es la de antes, te invito a descubrir cómo el biomagnetismo puede ayudarte a volver a tu centro vital.</p>
<!-- /wp:paragraph -->"""
        },
        2: {
            "title": "¿Qué es el Par Biomagnético? La Revolución del Bipolo Magnético",
            "excerpt": "Entiende el mecanismo real detrás del Par Biomagnético: resonancia, equilibrio de pH y eliminación de patógenos. Más que imanes, es bioenergética pura.",
            "content": """<!-- wp:paragraph -->
<p>Como terapeuta especializada en <strong>salud bioenergética</strong>, he verificado cómo el <strong>Par Biomagnético</strong> ha transformado la vida de miles de personas. No es una técnica de magnetoterapia común; es un sistema de diagnóstico y tratamiento que utiliza el magnetismo para detectar y corregir desequilibrios de pH en el organismo. Mi misión es ayudar al cuerpo a recuperar su armonía natural, creando un entorno donde el bienestar sea la norma y no la excepción.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>El Descubrimiento del Dr. Isaac Goiz Durán</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>En 1988, el Dr. Isaac Goiz descubrió que las enfermedades se asocian a una distorsión del pH en dos puntos específicos del cuerpo que entran en <strong>resonancia vibracional</strong>. A este conjunto lo llamó 'Par Biomagnético'. Su gran hallazgo fue entender que mientras un punto se acidifica (debido a la presencia de virus o hongos), el otro se alcaliniza simultáneamente (favoreciendo bacterias o parásitos).</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>¿Cómo funciona realmente la terapia?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>La esencia de esta técnica es el <strong>bipolo magnético</strong>. Durante una sesión, realizamos un <strong>rastreo bioenergético</strong> minucioso (test kinesiológico) para identificar estos desequilibrios. Al colocar un imán de polo Norte (negativo) y otro de polo Sur (positivo) en los puntos que resuenan, generamos un flujo de electrones que neutraliza la zona de forma casi instantánea.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>La Diferencia con la Magnetoterapia</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Mucha gente confunde ambas, pero el Par Biomagnético es mucho más específico:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
<li><strong>Específicidad:</strong> Buscamos el par exacto que origina el síntoma.</li>
<li><strong>Intensidad:</strong> Usamos imanes de neodimio de alta potencia (más de 1000 Gauss).</li>
<li><strong>Causa Raíz:</strong> Actuamos sobre la simbiosis de microorganismos patógenos.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Beneficios Sistémicos del Par Biomagnético</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Al regular el pH, estamos impactando positivamente en prácticamente todos los sistemas del cuerpo:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
<li><strong>Sistema Inmune:</strong> Al eliminar la carga patógena, el cuerpo puede defenderse mejor.</li>
<li><strong>Sistema Circulatorio:</strong> Mejora el flujo sanguíneo y la oxigenación de los tejidos.</li>
<li><strong>Equilibrio Emocional:</strong> Muchos bloqueos físicos tienen una raíz emocional que liberamos en consulta.</li>
<li><strong>Energía Vital:</strong> Al optimizar la química celular, el cansancio desaparece.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>¿Qué afecciones se pueden tratar?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Aunque el biomagnetismo no trata 'enfermedades' sino 'personas', sus resultados son excelentes en:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
<li><strong>Problemas Digestivos:</strong> Como la gastritis por <a href="/blog/h-pylori">Helicobacter Pylori</a>.</li>
<li><strong>Alergias:</strong> Resetando la respuesta exagerada del sistema inmunitario.</li>
<li><strong>Dolores Crónicos:</strong> Fibromialgia, migrañas y dolores articulares.</li>
<li><strong>Trastornos del Sueño:</strong> Regulando el sistema nervioso autónomo.</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>El Par Biomagnético es un <strong>camino hacia la salud integral</strong> que respeta la sabiduría de tu organismo. Si buscas una alternativa natural, segura y profunda para recuperar tu equilibrio, te invito a conocer mi método de trabajo en las <a href="/tratamientos">sesiones de terapia personalizada</a>.</p>
<!-- /wp:paragraph -->"""
        },
        42: {
            "title": "Helicobacter Pylori: La Estrategia Magnética para su Eliminación",
            "excerpt": "¿Vives con acidez constante? La Helicobacter Pylori es una bacteria experta en camuflaje. Descubre cómo el Par Biomagnético neutraliza su ambiente sin antibióticos agresivos.",
            "content": """<!-- wp:paragraph -->
<p>La <strong>Helicobacter pylori (H. pylori)</strong> es una de las bacterias más exitosas y peligrosas que habitan en el ser humano. Se estima que más de la mitad de la población mundial está infectada. Como especialista en salud integrativa, trato habitualmente a pacientes que han pasado por múltiples ciclos de antibióticos sin éxito. El problema no es la bacteria en sí, sino el <strong>terreno gástrico</strong> que le permite esconderse.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>¿Por qué es tan resistente la H. Pylori?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Esta bacteria tiene una habilidad fascinante: produce una enzima llamada ureasa que neutraliza el ácido del estómago a su alrededor, creando una 'burbuja' alcalina protectora. Al vivir bajo la mucosa gástrica, los antibióticos a menudo no llegan con la concentración suficiente, o la bacteria desarrolla resistencias rápidamente.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>El Abordaje del Par Biomagnético</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>En las sesiones de <a href="/">Par Biomagnético</a>, no buscamos 'matar' directamente a la bacteria, sino <strong>neutralizar el pH</strong> de los puntos donde resuena. El Dr. Goiz identificó pares específicos (como Hiato Esofágico - Testículo/Vagina) que están asociados a esta patología. Al aplicar los imanes:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
<li>Eliminamos la burbuja protectora de la bacteria.</li>
<li>Restablecemos la acidez natural del estómago que es hostil para ella.</li>
<li>Mejoramos la capacidad inmunitaria de la mucosa gástrica.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Síntomas que indican su presencia</h2>
<!-- /wp:heading -->

<p>Muchos pacientes no saben que la tienen hasta que el daño es severo. Atenta a estas señales:</p>
<!-- wp:list -->
<ul>
<li>Ardor o dolor punzante en el abdomen superior.</li>
<li>Hinchazón persistente después de comer (meteorismo).</li>
<li>Náuseas, especialmente por la mañana.</li>
<li>Eructos frecuentes y mal aliento.</li>
<li>Anemia inexplicable o fatiga crónica (por mala absorción de B12).</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h3>Relación con las Migrañas</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Es sorprendente para muchos, pero existe una conexión directa entre la infección por H. Pylori y las migrañas crónicas. Las toxinas generadas por la bacteria pasan al torrente sanguíneo, afectando al sistema nervioso. He visto cómo al tratar el par gástrico, los dolores de cabeza desaparecen. Puedes leer más sobre esto en mi artículo sobre <a href="/blog/tratamiento-dolor-cabeza">dolores de cabeza y biomagnetismo</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Recuperación Post-Tratamiento</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Una vez que neutralizamos la bacteria magnéticamente, es vital reconstruir el terreno:</p>
<ol>
<li><strong>Probióticos:</strong> Para repoblar la flora beneficiosa.</li>
<li><strong>Alimentación Alcalinizante:</strong> Para evitar que el estómago vuelva a ser un nido de patógenos.</li>
<li><strong>Gestión Emocional:</strong> El estómago es nuestro 'segundo cerebro'; el estrés es el mejor aliado de la H. Pylori.</li>
</ol>

<!-- wp:paragraph -->
<p>Si estás cansado de los tratamientos convencionales y buscas una solución profunda y natural, el biomagnetismo médico ofrece una vía de sanación real para tu sistema digestivo.</p>
<!-- /wp:paragraph -->"""
        },
        55: {
            "title": "¿Es posible el Par Biomagnético a distancia? Ciencia Cuántica y Sanación",
            "excerpt": "¿Se pueden usar imanes a miles de kilómetros? Descubre la ciencia del entrelazamiento cuántico y cómo funciona la terapia de Par Biomagnético a distancia con la misma eficacia.",
            "content": """<!-- wp:paragraph -->
<p>La terapia de <strong>Par Biomagnético a distancia</strong> suele despertar escepticismo inicial: ¿Cómo es posible que un terapeuta en España trate a un paciente en América sin contacto físico? La respuesta no está en la magia, sino en las fronteras de la <strong>física cuántica</strong> y la bioenergética moderna.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>El Entrelazamiento Cuántico: La Base Científica</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>La física cuántica ha demostrado que dos partículas que han estado en contacto pueden quedar 'entrelazadas'. Lo que le sucede a una afecta instantáneamente a la otra, sin importar la distancia (un fenómeno que Einstein llamó 'acción fantasmal a distancia'). En terapia, utilizamos este principio para establecer una conexión bionergética entre el terapeuta y el paciente a través de la <strong>intención dirigida</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>El Terapeuta como Antena Biológica</h2>
<!-- /wp:heading -->

<p>En una sesión remota, el terapeuta utiliza un 'sustituto' (que puede ser el propio cuerpo del terapeuta o un tercero) para realizar el rastreo. El cuerpo del paciente, a nivel energético, responde a las preguntas del test kinesiológico revelando dónde están los desequilibrios de pH. Es un fenómeno de <strong>resonancia bionergética</strong>.</p>

<!-- wp:heading -->
<h2>¿Cómo se aplican los imanes a distancia?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Al aplicar los pares magnéticos sobre el sustituto, la información de corrección se transmite al paciente. La energía no conoce de barreras geográficas; solo de frecuencias. Los resultados en mis sesiones online han demostrado ser tan potentes y duraderos como los de la consulta presencial en Monzón.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Ventajas de la Terapia Online</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul>
<li><strong>Comodidad absoluta:</strong> Recibes la sanación en tu propio sofá o cama, favoreciendo un estado de relajación profunda.</li>
<li><strong>Sin desplazamientos:</strong> Ideal para personas con movilidad reducida o que viven en otros países.</li>
<li><strong>Eficacia probada:</strong> La despolarización del pH ocurre en tiempo real, independientemente de los kilómetros.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>¿Qué necesito para una sesión a distancia?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Solo necesitas un espacio tranquilo donde no te interrumpan y una conexión a internet para la entrevista inicial. Como especialista, te guiaré durante todo el proceso para que la experiencia sea cercana y transformadora. La sanación cuántica es el futuro de la medicina integrativa, y hoy está a tu alcance.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class=\"wp-block-buttons\">
<div class=\"wp-block-button\"><a class=\"wp-block-button__link\" href=\"/tratamientos\">Reservar mi Sesión Cuántica</a></div>
</div>
<!-- /wp:buttons -->"""
        }
    }

    count = 0
    for post in posts:
        if post['id'] in new_content:
            post.update(new_content[post['id']])
            count += 1
    
    with open('src/data/posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    
    print(f"Updated {count} posts.")

update_posts()
