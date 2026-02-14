PORTNAME=	domainhunter
DISTVERSION=	51.38cb7ef
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Checks expired domains for categorization/reputation and Archive.org history to determine good candidates for phishing and C2 domain names.
WWW=		https://github.com/threatexpress/domainhunter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pytesseract@${PY_FLAVOR} \
		??/py-texttable@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
