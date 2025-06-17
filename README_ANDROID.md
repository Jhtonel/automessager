# 📱 WhatsApp Auto Sender - Versão Android (Standalone)

Esta é uma versão otimizada para dispositivos móveis Android da aplicação de envio automático de mensagens via WhatsApp Web.

## 🚀 Como Usar no Android (Sem Computador)

### Método 1: Hospedagem Gratuita (Recomendado)

1. **Faça upload do arquivo `app_android_standalone.html` para um serviço de hospedagem gratuita:**
   - [Netlify Drop](https://app.netlify.com/drop) (arraste o arquivo e use o link gerado)
   - [Vercel](https://vercel.com/) (crie um projeto estático)
   - [GitHub Pages](https://pages.github.com/) (faça upload em um repositório público)

2. **Abra o link gerado no navegador do seu Android.**
   - Você pode adicionar à tela inicial para virar um "app".

3. **Use normalmente:**
   - Faça upload do CSV ou adicione contatos manualmente.
   - Configure as mensagens e envie via WhatsApp Web.

### Método 2: Aplicativo Web Progressivo (PWA)

Para uma experiência mais nativa, você pode instalar a aplicação como PWA:

1. Abra a aplicação no Chrome do Android
2. Toque no menu (3 pontos) → "Adicionar à tela inicial"
3. A aplicação aparecerá como um app normal

## 📋 Pré-requisitos

- **Navegador moderno** (Chrome, Firefox, Safari)
- **WhatsApp Web** logado no navegador
- **Arquivo CSV** com colunas: `telefone,nome` (ou adicione manualmente)
- **Conexão com internet** estável

## 📁 Formato do Arquivo CSV

Seu arquivo CSV deve ter este formato:

```csv
telefone,nome
5511999999999,João Silva
5511888888888,Maria Santos
5511777777777,Pedro Oliveira
```

**Importante:**
- Use o código do país (55 para Brasil)
- Não use espaços ou caracteres especiais no telefone
- O nome pode conter espaços e acentos

## 🔧 Funcionalidades

### ✅ Recursos Disponíveis

- **Interface responsiva** otimizada para touch
- **Múltiplos templates** de mensagem
- **Upload de CSV** direto do dispositivo
- **Adição manual de contatos**
- **Controle de progresso** em tempo real
- **Memória local** para evitar reenvios
- **Configuração de delay** entre mensagens
- **Validação de dados** automática

### 📱 Otimizações para Mobile

- **Design touch-friendly** com botões grandes
- **Navegação por gestos** suportada
- **Interface adaptativa** para diferentes tamanhos de tela
- **Feedback visual** para todas as ações
- **Carregamento otimizado** para conexões móveis

## ⚠️ Limitações e Considerações

### Limitações Técnicas

1. **Navegadores móveis** podem bloquear popups automáticos
2. **WhatsApp Web** pode detectar uso automatizado
3. **Taxa de envio** limitada para evitar spam
4. **Dependência** de conexão estável

### Recomendações de Uso

1. **Use delays adequados** (5-10 segundos entre mensagens)
2. **Não envie em massa** - distribua ao longo do dia
3. **Mantenha o WhatsApp Web ativo** durante o processo
4. **Teste com poucos contatos** primeiro
5. **Respeite as políticas** do WhatsApp

## 🛠️ Solução de Problemas

### Problema: Popups bloqueados
**Solução:** Permita popups no navegador para o site

### Problema: WhatsApp Web não carrega
**Solução:** Verifique se está logado e a conexão estável

### Problema: Arquivo CSV não carrega
**Solução:** Verifique o formato e codificação (UTF-8)

### Problema: Mensagens não são enviadas
**Solução:** Aumente o delay entre mensagens

## 🔒 Segurança e Privacidade

- **Dados processados localmente** - nada é enviado para servidores externos
- **Números processados** salvos apenas no dispositivo
- **Arquivos CSV** não são armazenados permanentemente
- **Sem rastreamento** ou coleta de dados pessoais

## 📞 Suporte

Se encontrar problemas:

1. Verifique se o WhatsApp Web está funcionando
2. Teste com um arquivo CSV pequeno primeiro
3. Verifique a conexão com a internet
4. Tente em um navegador diferente

## 🔄 Atualizações

Para atualizar a aplicação:

1. Substitua o arquivo `app_android_standalone.html` pela nova versão
2. Limpe o cache do navegador se necessário
3. Recarregue a página

---

**Nota:** Esta aplicação é para uso pessoal e educacional. Respeite sempre as políticas de uso do WhatsApp e as leis de proteção de dados. 