PORTNAME=	jira-scan
DISTVERSION=	7.447d0ec
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A simple remote scanner for Atlassian Jira
WWW=		https://github.com/bcoles/jira_scan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ruby-pkg-config \
		??/ruby-terminal-table \
		lang/ruby \
		sysutils/rubygem-bundler \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
