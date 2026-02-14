PORTNAME=	smbsr
DISTVERSION=	50.7f86241
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Lookup for interesting stuff in SMB shares.
WWW=		https://github.com/oldboy21/SMBSR

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ldap3@${PY_FLAVOR} \
		??/py-ldap@${PY_FLAVOR} \
		??/py-masscan@${PY_FLAVOR} \
		??/py-pysmb@${PY_FLAVOR} \
		??/py-textract@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
