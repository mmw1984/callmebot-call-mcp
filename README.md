# CallMeBot Telegram Voice Call MCP Server

An MCP (Model Context Protocol) server for making voice calls to Telegram users via CallMeBot API with Text-to-Speech (TTS).

## Features

- Make voice calls to Telegram users
- Support for multiple languages and voices
- Configurable repeat count
- Text message carbon copy options
- Call timeout configuration
- API Key authentication

## Deploy to Vercel

### 1. Install Vercel CLI

```bash
npm install -g vercel
```

### 2. Login to Vercel

```bash
vercel login
```

### 3. Deploy

```bash
vercel --prod
```

### 4. Set Environment Variables

Set `MCP_API_KEY` environment variable in Vercel dashboard.

## Local Development

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables

Copy `.env.example` to `.env` and set your API Key:

```bash
cp .env.example .env
```

### 3. Run

```bash
python run_local.py
```

## Client Configuration

### Claude Desktop (Remote)

```json
{
  "mcpServers": {
    "callmebot": {
      "url": "https://your-vercel-app.vercel.app/mcp"
    }
  }
}
```

### Claude Desktop (Local)

```json
{
  "mcpServers": {
    "callmebot": {
      "command": "python",
      "args": ["-m", "run_local"],
      "cwd": "/path/to/callmebot-call-mcp"
    }
  }
}
```

## MCP Tool

### `call_telegram_user`

Make a voice call to a Telegram user with TTS.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | MCP server API Key for authentication |
| `username` | string | Yes | Telegram username (e.g. @myuser) or phone number (e.g. +331234567890) |
| `text` | string | Yes | Text message to be spoken (max 256 characters) |
| `lang` | string | No | Voice language (default: en-US-Standard-B) |
| `repeat` | int | No | Number of times to repeat (default: 2) |
| `carbon_copy` | string | No | Text copy option: yes/no/missed/only (default: yes) |
| `timeout` | int | No | Call timeout in seconds (default: 30) |

## Common Language Codes

| Language | Voice Code |
|----------|------------|
| English (US) | en-US-Standard-B |
| English (UK) | en-GB-Standard-B |
| Cantonese (HK) | yue-HK-Standard-A |
| Mandarin Chinese | cmn-CN-Standard-A |
| Japanese | ja-JP-Standard-A |
| Korean | ko-KR-Standard-A |
| German | de-DE-Standard-B |
| French | fr-FR-Standard-B |
| Spanish | es-ES-Standard-B |

## Carbon Copy Options

| Option | Description |
|--------|-------------|
| `yes` | Always send a text message copy (default) |
| `no` | Do not send a text message copy |
| `missed` | Only send text message if call is missed or rejected |
| `only` | Only send text message (dedicated bots only) |

## Prerequisites

1. **Authorize CallMeBot**: Send `/start` to @CallMeBot_txtbot on Telegram before using.

2. **iOS Bug**: There is a known VoIP protocol issue with Telegram iOS that may prevent audio playback.

3. **Text Limit**: Text message is limited to 256 characters.

## License

MIT
