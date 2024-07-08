from flask import render_template, request, jsonify, redirect, url_for
from .services.search_service import get_urls
from .services.document_service import load_documents, process_documents
from .services.chat_service import create_chat_logic, ask_question, format_output_to_html
from .services.preview_service import fetch_webpage_content

def init_routes(app, socketio):

    @app.route('/')
    def index():
        return render_template('AI.html')

    @app.route ( '/login3.html' )
    def login3():
        return render_template ( 'login3.html' )

    @app.route('/index.html')
    def index1():
        return render_template('index.html')

    @app.route ( '/try_it_yourself', methods=['GET', 'POST'] )
    def try_it_yourself():
        if request.method == 'POST':
            # Perform login logic
            # Assuming login is successful, redirect to index.html
            if request.method == 'POST':
                if 'login_email' in request.form:
                    email = request.form['login_email']
                    password = request.form['login_pass']
                    if email in users and users[email][0] == password:
                        return redirect ( url_for ( 'index.html' ) )
                    else:
                        return render_template ( 'index.html' )

    @app.route('/process_query', methods=['POST'])
    def process_query():
        query = request.json.get('query')
        print('Query received: ', query)
        urls = get_urls(query)
        print('URLs fetched: ', urls)
        docs_list = load_documents(urls)
        retriever = process_documents(docs_list)
        chat_logic_chain = create_chat_logic(retriever)
        answer = ask_question(chat_logic_chain, query)
        print('Answer generated: ', answer)

        formatted_answer = format_output_to_html(answer)

        return jsonify({
            'answer': formatted_answer,
            'urls': urls
        })

    @app.route('/preview')
    def preview():
        url = request.args.get('url')
        if not url:
            return jsonify({'error': 'URL parameter is missing'}), 400

        content = fetch_webpage_content(url)
        if content:
            return content, 200, {'Content-Type': 'text/html; charset=utf-8'}
        else:
            return jsonify({'error': 'Failed to fetch the webpage'}), 500

    # @app.route('/login3')
    # def login3():
    #     return render_template('login3.html')
    #
    # @app.route('/try_it_yourself', methods=['GET', 'POST'])
    # def try_it_yourself():
    #     if request.method == 'POST':
    #         # Perform login logic
    #         # Assuming login is successful, redirect to index.html
    #         if request.method == 'POST':
    #             if 'login_email' in request.form:
    #                 email = request.form['login_email']
    #                 password = request.form['login_pass']
    #                 if email in users and users[email][0] == password:
    #                     return redirect(url_for('index'))
    #                 else:
    #                     return render_template('index.html')

