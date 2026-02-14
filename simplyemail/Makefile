PORTNAME=	simplyemail
DISTVERSION=	1.4.10.r7.6a42d37
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Email recon made fast and easy, with a framework to build on CyberSyndicates.
WWW=		https://github.com/killswitch-GUI/SimplyEmail

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/antiword \
		??/odt2txt \
		??/py-beautifulsoup3@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-configparser@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-docx2txt@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-pdfminer@${PY_FLAVOR} \
		??/py-xlsx2csv@${PY_FLAVOR} \
		ftp/wget \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
