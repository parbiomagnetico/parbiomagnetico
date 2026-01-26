import json

def update_posts_batch10():
    with open('src/data/posts.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)

    new_content = {
        4: {
            "title": "Diccionario del Biomagnetismo: Hablando el Idioma de la Sanación",
            "excerpt": "¿Qué es un rastreo? ¿Qué significa NEN o Bipolo? Domina la terminología experta para entender tu proceso de curación con imanes.",
            "content": """<!-- wp:paragraph --><p>Entrar en el mundo del **Par Biomagnético** puede sentirse al principio como aprender un nuevo idioma. Como terapeuta, considero fundamental que el paciente entienda los términos que usamos en consulta, ya que esa comprensión activa tu propia inteligencia biológica en el proceso de sanación. Aquí tienes los conceptos clave que debes conocer:</p><!-- /wp:paragraph --><ul><li><strong>NEN (Nivel Energético Normal):</strong> Es la neutralidad del pH (alrededor de 7) donde no existe enfermedad.</li><li><strong>Rastreo Bioenergético:</strong> El escaneo completo del cuerpo mediante kinesiología para localizar puntos de desequilibrio.</li><li><strong>Bipolo:</strong> El conjunto de dos puntos que están en resonancia (uno ácido y otro alcalino). No se puede tratar un punto sin su pareja.</li><li><strong>Despolarización:</strong> El fenómeno físico del retorno al equilibrio del pH mediante los imanes.</li><li><strong>Crisis de Curación:</strong> Una breve reacción del cuerpo al eliminar toxinas tras la sesión; señal inequívoca de que la curación ha comenzado.</li></ul>"""
        },
        7: {
            "title": "¿Cómo se siente una Sesión de Par Biomagnético? Tu Viaje al Equilibrio",
            "excerpt": "Relajación, paz y conexión. Descubre paso a paso qué ocurre en una consulta y cómo tu cuerpo responde a la energía magnética.",
            "content": """<!-- wp:paragraph --><p>Mucha gente acude a su primera sesión con cierta intriga: ¿Dolerá? ¿Sentiré electricidad? La respuesta es una profunda relajación. Una sesión de **Par Biomagnético** es, ante todo, un tiempo para ti, para que tu cuerpo sea escuchado sin las prisas del día a día.</p><!-- /wp:paragraph --><h2>¿Qué ocurre durante la consulta?</h2><p>Te tumbarás en una camilla, completamente vestido y con calzado adecuado (preferiblemente zapato cerrado para el testaje). Durante los aproximadamente 60-90 minutos:</p><ul><li><strong>El Rastreo:</strong> Iré preguntando bionergéticamente a tu cuerpo mientras observo la respuesta de tus extremidades. Tu cuerpo revela su verdad química sin que tengas que decir una palabra.</li><li><strong>La Impactación:</strong> Una vez detectados los pares, colocaré los imanes sobre los puntos específicos. Sentirás una agradable sensación de descanso; muchos pacientes llegan a quedarse dormidos.</li><li><strong>El Reposo Magnético:</strong> Los imanes harán su trabajo de equilibrar tu pH mientras tú simplemente respiras y permites el cambio.</li></ul><p>Al finalizar, te sentirás más ligero y con una mayor sensación de claridad. Es el inicio de tu <a href="/blog/como-son-las-sesiones">restauración biológica</a>.</p>"""
        },
        17: {
            "title": "Dr. Isaac Goiz Durán: El Hombre que Descubrió el Mapa de la Salud",
            "excerpt": "Homenaje al descubridor del Par Biomagnético. Conoce la historia de una de las mentes más brillantes de la medicina alternativa del siglo XX.",
            "content": """<!-- wp:paragraph --><p>No podemos hablar de biomagnetismo sin rendir tributo a su creador, el **Dr. Isaac Goiz Durán**. En 1988, este médico y fisioterapeuta mexicano realizó un hallazgo que cambiaría la medicina integrativa para siempre: el primer Par Biomagnético (Sida-Sida). Su visión superó la medicina tradicional al entender que la salud no depende de agentes aislados, sino del equilibrio magnético y vibracional de los órganos en resonancia.</p><!-- /wp:paragraph --><h2>Un Legado de Sanación Global</h2><p>El Dr. Goiz dedicó su vida a codificar el código del Par Biomagnético, rastreando miles de pacientes y formando a terapeutas en todo el mundo. Su gran aportación fue democratizar la salud, proporcionando una técnica segura, eficaz y no invasiva que hoy ayuda a millones de personas. Como terapeuta formada en su metodología, mi compromiso es mantener la pureza y el rigor de su descubrimiento en cada sesión que realizo.</p>"""
        },
        23: {
            "title": "Acidosis y Osteoporosis: Por qué tus Huesos Necesitan un pH Equilibrado",
            "excerpt": "¿Sabías que el cuerpo roba calcio de tus huesos para neutralizar la acidez de la sangre? Aprende a prevenir la descalcificación con imanes.",
            "content": """<!-- wp:paragraph --><p>La osteoporosis a menudo se trata solo como una falta de calcio, pero la pregunta clave es: ¿Por qué se fue ese calcio de tus huesos? La respuesta suele ser la **acidosis metabólica**. Tu sangre tiene una prioridad absoluta: mantener su pH entre 7.35 y 7.45 para sobrevivir. Si tu dieta o el estrés acidifican tu terreno interno, el cuerpo entra en modo emergencia y 'disuelve' un poco de hueso para liberar minerales alcalinos (calcio) que neutralicen ese ácido gástrico y sanguíneo.</p><!-- /wp:paragraph --><h2>Protegiendo tu Estructura con Biomagnetismo</h2><p>El Par Biomagnético ayuda a detener este proceso de 'erosión' ósea. Al equilibrar el pH de los órganos maestros de filtración (riñón e hígado), permitimos que el cuerpo deje de recurrir a sus reservas estructurales. Un pH equilibrado es la mejor protección para tus huesos, permitiendo que el calcio se fije donde realmente pertenece. No solo tomes suplementos, <a href="/blog/la-importancia-vital-de-un-ph-equilibrado">corrige el terreno que los expulsa</a>.</p>"""
        },
        48: {
            "title": "Asma y Capacidad Pulmonar: El Aliento de la Vida Recuperado",
            "excerpt": "No te conformes con los inhaladores. Descubre cómo el biomagnetismo ayuda a desinflamar los bronquios y a eliminar la raíz patógena del asma.",
            "content": """<!-- wp:paragraph --><p>El **asma** es la expresión de un sistema respiratorio en estado de hiperreactividad y espasmo. Ya sea de origen alérgico, emocional o infeccioso, el asma genera un pH ácido en las mucosas bronquiales que perpetúa la inflamación. En mi consulta, trabajamos para que puedas volver a respirar hondo, eliminando el terreno que favorece el cierre de las vías respiratorias.</p><!-- /wp:paragraph --><h2>Abordaje Magnético del Asma</h2><p>Mediante el rastreo, identificamos si existen microorganismos (como micoplasmas o virus respiratorios) en simbiosis que estén irritando los pulmones. Al colocar los imanes en pares como Pulmón-Pulmón o Condral-Condral, logramos una relajación muscular y una desinflamación profunda. Al recuperar la neutralidad biológica, la frecuencia de las crisis disminuye drásticamente, permitiendo que recuperes tu energía y tu libertad de movimiento.</p>"""
        }
    }

    count = 0
    for post in posts:
        if post['id'] in new_content:
            post.update(new_content[post['id']])
            count += 1
    
    with open('src/data/posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    
    print(f"Updated {count} posts batch 10.")

update_posts_batch10()
