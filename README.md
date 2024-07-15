# stapp-lchain-groq-agents
[langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent)を参考に、Groq-APIを利用したアプリを作ってみる

## コンテンツ
- サンプルコード（[streamlit-example](https://github.com/streamlit/streamlit-example)）
### (langchain-ai)streamlit-agents examples

- `basic_streaming.py`: Simple streaming app with `langchain.chat_models.ChatOpenAI` ([View the app](https://langchain-streaming-example.streamlit.app/))
- `basic_memory.py`: Simple app using `StreamlitChatMessageHistory` for LLM conversation memory ([View the app](https://langchain-st-memory.streamlit.app/))
- `mrkl_demo.py`: An agent that replicates the [MRKL demo](https://python.langchain.com/docs/modules/agents/how_to/mrkl) ([View the app](https://langchain-mrkl.streamlit.app))
- `minimal_agent.py`: A minimal agent with search (requires setting `OPENAI_API_KEY` env to run)
- `search_and_chat.py`: A search-enabled chatbot that remembers chat history ([View the app](https://langchain-chat-search.streamlit.app/))
- `simple_feedback.py`: A chat app that allows the user to add feedback on responses using [streamlit-feedback](https://github.com/trubrics/streamlit-feedback), and link to the traces in [LangSmith](https://docs.smith.langchain.com/) ([View the app](https://langsmith-simple-feedback.streamlit.app/))
- `chat_with_documents.py`: Chatbot capable of answering queries by referring custom documents ([View the app](https://langchain-document-chat.streamlit.app/))
- `chat_with_sql_db.py`: Chatbot which can communicate with your database ([View the app](https://langchain-chat-sql.streamlit.app/))
- `chat_pandas_df.py`: Chatbot to ask questions about a pandas DF (Note: uses `PythonAstREPLTool` which is vulnerable to arbitrary code execution,
  see [langchain #7700](https://github.com/langchain-ai/langchain/issues/7700))

Apps feature LangChain 🤝 Streamlit integrations such as the
[Callback integration](https://python.langchain.com/docs/modules/callbacks/integrations/streamlit) and
[StreamlitChatMessageHistory](https://python.langchain.com/docs/integrations/memory/streamlit_chat_message_history).



## Usage
- [poetry cli](https://cocoatomo.github.io/poetry-ja/cli/)を利用する

### Setup
```sh
poetry install
poetry shell
```

### コマンド一覧
```sh
$ task --list
start        streamlit run src/main.py
test         pytest tests
test-cov     pytest tests --cov --cov-branch -svx
test-repo    pytest tests --cov --cov-report=html
format       black --line-length 79 src
lint         flake8 src
check-format black整形とflake8チェックを実行
```

### Start as local service
```sh
# on poetry shell
# streamlit hello
# streamlit run src/main.py
task start
# Local URL: http://localhost:8501
```


### format and lint check
```sh
# task format
# task lint
task check-format
```


### Test with `pytest`
- [streamlitのテスト手法](https://docs.streamlit.io/develop/concepts/app-testing/get-started)を参考にテストを実施
```sh
# on poetry shell
# pytest tests/test_main.py
task test
```

### Test coverage

#### show c1 coverage
```sh
# on poetry shell
task test-cov
```

#### output HTML coverage report
```sh
# on poetry shell
task test-repo
```


## 使用ライブラリ

このプロジェクトは以下のオープンソースライブラリを使用しています：

- [Streamlit](https://streamlit.io/) - Apache License 2.0

  Copyright © 2019-2024 Streamlit Inc.

  Streamlitは、データアプリケーションを簡単に作成するためのオープンソースライブラリです。

### 参考コード
このプロジェクトは以下のサンプルコードを参考にしています

- [langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent)
- LangChain：[ChatModel > Groq](https://python.langchain.com/v0.2/docs/integrations/chat/groq/)

## ライセンス
Apache 2.0

このプロジェクトは Apache 2.0 ライセンスの下で公開されています。詳細は [LICENSE](./LICENSE) ファイルをご覧ください。

ただし、このプロジェクトは Apache License 2.0 でライセンスされている Streamlit を使用しています。
Streamlit のライセンス全文は [こちら](https://github.com/streamlit/streamlit/blob/develop/LICENSE) でご確認いただけます。
